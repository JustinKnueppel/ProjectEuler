open! Solution

let ( << ) f g x = f (g x)
let print_sln = print_endline << Int.to_string << solve

let () =
  print_sln 10;
  print_sln 1000
