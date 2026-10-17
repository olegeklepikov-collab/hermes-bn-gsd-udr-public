#!/bin/bash
set -eu
bundle_root=$(cd "$(dirname "$0")/.." && pwd)
source "$bundle_root/runtime/Hermes BN/environment.sh"
exec "$HERMES_BN_ROOT/bin/hermes-bn" setup
