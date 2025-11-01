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

module IntMap = Map.Make (Int)

let freqs xs =
  List.fold_left
    (fun acc x ->
      IntMap.update x
        (fun old ->
          match old with Some count -> Some (count + 1) | None -> Some 1)
        acc)
    IntMap.empty xs

let pp_map =
  IntMap.iter (fun num count ->
      print_endline (Int.to_string num ^ ": " ^ Int.to_string count))

let rec range high = if high <= 1 then [ 1 ] else high :: range (high - 1)
let ( << ) f g x = f (g x)
let rec pow x = function 1 -> x | y -> x * pow x (y - 1)
let combine_freqs fs = IntMap.fold (fun x count acc -> acc * pow x count) fs 1

let lowest_div_by_all high =
  List.map (freqs << all_factors) (range high)
  |> List.fold_left
       (fun final_freqs cur_freqs ->
         IntMap.fold
           (fun num count acc ->
             IntMap.update num
               (fun old ->
                 match old with
                 | Some old_count -> Some (max old_count count)
                 | None -> Some count)
               acc)
           final_freqs cur_freqs)
       IntMap.empty
  |> combine_freqs

let solve () = lowest_div_by_all 20
