exception No_Primes

let next_prime seq : int * int Seq.t =
  match seq () with
  | Seq.Nil -> raise No_Primes
  | Seq.Cons (x, rest) -> (x, Seq.filter (fun i -> i mod x <> 0) rest)

let nth_prime n =
  let rec loop primes n =
    let x, primes = next_prime primes in
    if n <= 1 then x else loop primes (n - 1)
  in
  loop (Seq.ints 2) n

let solve () = nth_prime 10_001
