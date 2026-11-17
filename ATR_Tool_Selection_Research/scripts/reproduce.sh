#!/usr/bin/env bash
set -euo pipefail
python -m unittest discover -s tests -v
python -m src.run_experiment
python -m src.plot_results
