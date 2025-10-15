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
            cp -r "templates/$1" "$2"
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
