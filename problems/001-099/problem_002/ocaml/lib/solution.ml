let fib_under n =
  let rec loop = function
    | fst :: snd :: rest ->
        let next = fst + snd in
        if next >= n then fst :: snd :: rest
        else loop @@ (next :: fst :: snd :: rest)
    | _ -> raise Exit
  in
  loop [ 2; 1 ]

let solve () =
  fib_under 4_000_000
  |> List.filter (fun x -> x mod 2 == 0)
  |> List.fold_left ( + ) 0
