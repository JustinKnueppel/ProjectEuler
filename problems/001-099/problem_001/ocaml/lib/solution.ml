let rec range n = if n <= 0 then [] else n :: range (n - 1)
let filter x = x mod 5 == 0 || x mod 3 == 0
let solve n = List.filter filter (range (n - 1)) |> List.fold_left ( + ) 0
