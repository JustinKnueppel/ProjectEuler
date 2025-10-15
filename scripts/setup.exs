Mix.install([{:req, "~> 0.5.0"}, {:htmd, "~> 0.2.0"}])

get_problem = fn number ->
  {:ok, %{body: body}} = Req.get("https://projecteuler.net/minimal=" <> number)
  body
end

convert_html = fn html ->
  {:ok, md} = Htmd.convert(html)
  md
end

build_out = fn number ->
  number = Integer.to_string(number)

  md =
    get_problem.(number)
    |> convert_html.()

  "# Problem #{number}\n\n[Link](https://projecteuler.net/problem=#{number})\n\n#{md}\n"
end

get_dir = fn num ->
  padded_num =
    num
    |> Integer.to_string()
    |> String.pad_leading(3, "0")

  dir =
    cond do
      num < 100 ->
        "001-099"

      num < 200 ->
        "100-199"

      num < 300 ->
        "200-299"

      num < 400 ->
        "300-399"

      num < 500 ->
        "400-499"

      num < 600 ->
        "500-599"

      num < 700 ->
        "600-699"

      num < 800 ->
        "700-799"

      num < 900 ->
        "800-899"

      num < 1000 ->
        "900-999"
    end

  "probs/#{dir}/problem_#{padded_num}"
end

write_readme = fn num ->
  data = build_out.(num)
  dir = get_dir.(num)

  File.mkdir_p!(dir)
  File.write!("#{dir}/README.md", data)
end

Enum.each(1..950, write_readme)
