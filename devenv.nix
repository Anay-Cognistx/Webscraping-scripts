{ pkgs, lib, config, inputs, ... }:

{
  env.FIREFOX_BINARY_PATH = "/opt/homebrew/bin/firefox";
  env.GECKODRIVER_PATH = "/nix/store/5whmd2phkhfqd13d278771ph4p44fdbn-geckodriver-0.36.0/bin/geckodriver";

}
