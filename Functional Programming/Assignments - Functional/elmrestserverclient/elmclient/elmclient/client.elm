import Html exposing (..)
import Html.Attributes exposing (..)
import Html.Events exposing (..)
import Http
import Json.Decode as Decode



main =
  beginnerProgram { model = 0, view = view, update = update }


-- MODEL

type alias Model =
  {
  counter : Int
  }


init : String -> (Model, Cmd Msg)
init counter =
  (
  Model counter 1
  )

-- VIEW

view model =
  div []
    [ button [ onClick getCount ] [ text "Get Count" ]
    , div [] [ text (toString model) ]
    , button [ onClick setCount ] [ text "Set Count" ]
    ]


-- UPDATE

type Msg
  = Count
  | NewCount (Result Http.Error String)


update : Msg -> Model -> (Model, Cmd Msg)
update msg model =
  case msg of
    Count ->
      (model, counte model.counter)

    NewCount (Ok newCount) ->
      (Model model.counter newCount, Cmd.none)

    NewCount (Err _) ->
      (model, Cmd.none)

-- HTTP

getCount : String -> Cmd Msg
getCount counter =
  let
    url =
      "http://localhost:8084/elmserver/api/elm/counter"
  in
    Http.send NewCount (Http.get url decodeJson)

decodeJson: Decode.Decoder String
decodeJson =
  Decode.at ["data"] Decode.string

  setCount : String -> Cmd Msg
  setCount counter =
    let
      url =
        "http://localhost:8084/elmserver/api/elm/counter/1"
    in
      Http.send NewCount (Http.get url decodeJson)

  decodeJson: Decode.Decoder String
  decodeJson =
    Decode.at ["data"] Decode.string
