{ pkgs, lib, config, inputs, ... }:

{
    env = {
        FIREFOX_BINARY_PATH = "/opt/homebrew/bin/firefox";
        GECKODRIVER_PATH = "${pkgs.geckodriver}/bin/geckodriver";
    };
    git-hooks.hooks.end-of-file-fixer.enable = true;
}
