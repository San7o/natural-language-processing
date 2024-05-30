{
  description = "Python venv development template";

  inputs = {
    utils.url = "github:numtide/flake-utils";
  };

  outputs = {
    self,
    nixpkgs,
    utils,
    ...
  }:
    utils.lib.eachDefaultSystem (system: let
      pkgs = import nixpkgs {inherit system;};
      pythonPackages = pkgs.python3Packages;
    in {
      devShells.default = pkgs.mkShell {
        name = "python-venv";
        venvDir = "./.venv";
        buildInputs = [

          # Libc is needed for many python packages
          pkgs.libstdcxx5
          pkgs.zlib
          pkgs.libGL
          pkgs.glib

          # A Python interpreter including the 'venv' module is required to bootstrap
          # the environment.
          pythonPackages.python

          # This executes some shell code to initialize a venv in $venvDir before
          # dropping into the shell
          pythonPackages.venvShellHook

          # Those are dependencies that we would like to use from nixpkgs, which will
          # add them to PYTHONPATH and thus make them accessible from within the venv.
          # pythonPackages.numpy
        ];

        LD_LIBRARY_PATH = "${pkgs.libstdcxx5}/lib:${pkgs.zlib}/lib:${pkgs.stdenv.cc.cc.lib}/lib:${pkgs.libGL}/lib";

        # Run this command, only after creating the virtual environment
        postVenvCreation = ''
          unset SOURCE_DATE_EPOCH
          pip install -r requirements.txt

        '';

        # Now we can execute any commands within the virtual environment.
        # This is optional and can be left out to run pip manually.
        postShellHook = ''
          # allow pip to install wheels
          unset SOURCE_DATE_EPOCH
        '';
      };
    });
}
