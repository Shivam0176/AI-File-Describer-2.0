# scripts/post-build.sh

# Install rustup with a recent nightly toolchain
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- --default-toolchain nightly -y

# Add cargo to the PATH for subsequent steps
export PATH="$HOME/.cargo/bin:$PATH"

# Reinstall the python packages to leverage the new rust toolchain
pip install -r requirements.txt