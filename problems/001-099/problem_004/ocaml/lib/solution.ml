let rev_string s =
  let len = String.length s in
  String.init len (fun n -> String.get s (len - n - 1))

let is_palindrome num =
  let s = Int.to_string num in
  s = rev_string s

let rec range min max = if min > max then [] else min :: range (min + 1) max

let max_palindrome low high =
  let interval = range low high in
  List.map (fun x -> List.map (fun y -> x * y) interval) interval
  |> List.flatten |> List.filter is_palindrome |> List.fold_left max 0

let solve () = max_palindrome 100 999
