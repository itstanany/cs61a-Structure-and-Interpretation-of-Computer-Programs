(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  'YOUR-CODE-HERE
  (car (cdr s))
)

(define (caddr s)
  'YOUR-CODE-HERE
  (car (cddr s))
)


(define (sign num)
  'YOUR-CODE-HERE
  (cond ((< num 0) -1) ((> num 0) 1) (else 0))
)


(define (square x) (* x x))

(define (pow x y)
  'YOUR-CODE-HERE

    (define (innerPower num power) 
    (if (= power 2) (square num) (square (pow num (/ power 2))))
  )

  (if (even? y) (innerPower x y) (* x (innerPower x (- y 1))))

  ;alternate-solution
  ;(cond ((= y 2) (square x)) ((even? y ) (square (pow x (/ y 2)))) ((odd? y) (* x (pow x (- y 1)))))
  )



