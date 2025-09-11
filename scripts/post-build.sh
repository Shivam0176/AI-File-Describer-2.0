#!/bin/sh

# Install rustup with the latest stable toolchain
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y

# Add cargo to the PATH
export PATH="$HOME/.cargo/bin:$PATH"

# Reinstall Python dependencies to use the new Rust toolchain
pip install -r requirements.txt