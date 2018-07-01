{-# LANGUAGE OverloadedStrings #-}
{-# LANGUAGE DeriveGeneric #-}
module Main where

import Network.Wai.Middleware.Cors
import Web.Scotty

import GHC.Generics
import Data.Aeson (ToJSON, FromJSON)

import Prelude hiding (id)
import Data.IntMap (IntMap)
import qualified Data.IntMap.Strict as IntMap
import Control.Monad.Trans.Class (lift)

-- MVAR
import Control.Concurrent ( newMVar
                          , readMVar
                          , takeMVar
                          , putMVar
                          )

-- Prelude is always loaded but hide id (function id in elm)
-- qualified like AS in sql, qualified or relative namespace
insertMember :: Member -> IntMap Member -> (Member, IntMap Member)

insertMember member intMap =
  if id member > IntMap.size intMap || id member == 0 then
    let
    m = Member ((IntMap.size intMap) + 1) (name member) (email member)
    in
      (m, IntMap.insert (id m) m intMap)
    else
      (member, IntMap.insert (id member) member intMap)

data Member = Member
  { id :: Int
  , name :: String
  , email :: String
  } deriving (Show, Generic)

instance ToJSON Member

instance FromJSON Member

main :: IO ()
main = do
  membersRef <- newMVar (IntMap.fromList [ (1, Member 1 "Kurt" "kurt@kurt.dk")
                                         , (2, Member 2 "Sonja" "so@so.dk")
                                         ])
  scotty 9000 $ do
    middleware simpleCors
    get "/hello/:name" $ do
      name <- param "name"
      html $ mconcat [ "<h1>Hello ", name, " from Scotty!</h1><hr/>"]
    get "/member/count" $ do
      members <- lift $ readMVar membersRef
      json (IntMap.size members)
    get "/member" $ do
      members <- lift $ readMVar membersRef
      json (IntMap.elems members)
    get "/member/:id" $ do
        idText <- param "id"
        let id = (read idText) :: Int
        members <- lift $ readMVar membersRef
        case IntMap.lookup id members of
         Just member ->
           json $ member
         Nothing ->
            html "Provide a valid id"
    post "/member" $ do
      member <- jsonData
      beforeMembers <- lift $ takeMVar membersRef
      let (updatedMember, afterMembers) = insertMember member beforeMembers
      lift $ putMVar membersRef afterMembers
      json updatedMember
