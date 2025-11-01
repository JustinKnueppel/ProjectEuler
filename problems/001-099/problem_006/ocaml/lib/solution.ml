let rec range min max = if min > max then [] else min :: range (min + 1) max
let sum_squares = List.fold_left (fun acc x -> acc + (x * x)) 0

let square_sum xs =
  let sum = List.fold_left ( + ) 0 xs in
  sum * sum

let solve () =
  let n = 100 in
  let nums = range 1 n in
  square_sum nums - sum_squares nums
