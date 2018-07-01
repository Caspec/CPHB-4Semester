## Lisp Assignment - Flatmap, map.

;;
;; Exercise
;; This assignment is about implementing map and flat map. Map means going
;; from one list to another and flatten means flattening a list of
;; lists into just a list. Flat map is a combination of both.
;; Your job is to implement map and flat map.
;;


;; Part 1 - Map
;; Map is basically just a function which runs through a list and copies it
;; into a new list. But while copying, it does something to the data. In
;; other words it 'maps' the elements in the original to the new elements in
;; the new list. Your function should take two arguments: a function and a list

(defun myMap (f l) (if(equal (car l)nil) l (cons (funcall f(car l))(myMap f (cdr l)))))

(write(myMap (lambda (a) (+ a 2)) (list 3 5 7 9))) ;; Should return: (5 7 9 11)


;; Part 2 - Flattening
;; Flat map is doing two things: it's first taking a list and then flattening
;; all the lists inside that list into one long list. Wait, let's take that
;; again. If you have a list 'l' which have two lists inside:
;;
;; l = [   [1]  ,  [4]   ]
;;         [2]     [5]
;;         [3]     [6]
;;
;; then 'flatten' on 'l' would mean:
;;
;; m = [ 1, 2, 3, 4, 5, 6 ]
;;

(defun myFlatten (l) (if (equal (car l)nil)l (append (car l)(myFlatten(cdr l)))))

(write (myFlatten (list (list 1 2 3) (list 4 5 6)))) ;; should be (1 2 3 4 5 6))


;; Part 3 - Flat mapping
;; Combining the mapping and the flattening part, your job now is to do both:
;; flatten the full list while also applying a function to the elements.
;;

- Not working atm.

(defun myFlatMap (f l) l (append (myFlatMap f (cdr l)(myMap f(car l))))))

(write (myFlatMap (lambda (a) (+ a 2)) (list (list 1 2 3) (list 4 5 6))))