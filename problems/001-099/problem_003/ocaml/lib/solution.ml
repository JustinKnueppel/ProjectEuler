let isqrt x = Float.to_int @@ sqrt @@ Float.of_int x

let lowest_factor x =
  let rec loop i =
    if i > isqrt x then 1 else if x mod i == 0 then i else loop @@ (i + 1)
  in
  loop 2

let all_factors x =
  let rec loop factors x' =
    match lowest_factor x' with
    | 1 -> x' :: factors
    | f -> loop (f :: factors) (x' / f)
  in
  loop [] x

let solve () = all_factors 600851475143 |> List.fold_left max Int.min_int
