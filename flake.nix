{
  description = "Project Euler solutions dev flake";

  inputs = {
    flake-parts.url = "github:hercules-ci/flake-parts";
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs =
    inputs@{ flake-parts, ... }:
    flake-parts.lib.mkFlake { inherit inputs; } {
      imports = [
      ];
      systems = [
        "x86_64-linux"
        "aarch64-linux"
        "aarch64-darwin"
        "x86_64-darwin"
      ];
      perSystem =
        {
          config,
          self',
          inputs',
          pkgs,
          system,
          ...
        }:
        let
          tpl = pkgs.writeShellScriptBin "tpl" ''
            find_nearest_flake() {
              local current_dir=$(pwd)
              local target_file="flake.nix"

              while [ "$current_dir" != "/" ]; do
                if [ -f "$current_dir/$target_file" ]; then
                  echo "$current_dir"
                  return
                fi
                current_dir=$(dirname "$current_dir")
              done

              # If no flake.nix is found, return the current directory
              echo "$current_dir"
            }

            cp -r "$(find_nearest_flake)/templates/$1" "$2"
          '';
          run = pkgs.writeShellScriptBin "run" ''
            dune exec ./solution.exe
          '';
        in
        {
          # Per-system attributes can be defined here. The self' and inputs'
          # module parameters provide easy access to attributes of the same
          # system.

          devShells.default = pkgs.mkShell {
            buildInputs = with pkgs; [
              # Custom commands
              tpl
              run

              # OCaml
              ocaml
              ocamlPackages.utop
              ocamlPackages.ocaml-lsp
              ocamlPackages.ocamlformat
              ocamlPackages.findlib
              ocamlPackages.odoc
              dune_3
            ];
          };
        };
      flake = { };
    };
}
