#!/usr/bin/env python
#
# Computer Engineering Department, Bu-Ali University, Hamadan, Iran
# Computer Architecture Final Project Template
# Course supervisor and Instructor: Dr. M. Abbasi
# Designed by Neda Motamediraad, Graduate Teaching Assistant
# github.com/nedaraad/TinyProcessorSimulator
# under MIT licence

import sys
from simulator import TinyBASUSimulator as Simulator


def main():
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 6:
        print("Usage: python sim.py [total_cycles] [prediction_method] [inst_file] [data_file] [report_file]")
        return

    # Extract the command-line arguments
    timeout_cycles = int(sys.argv[1])
    prediction_method = sys.argv[2]
    inst_file = sys.argv[3]
    data_file = sys.argv[4]
    report_file = sys.argv[5]

    simulator = Simulator(prediction_method)
    simulator.parse_instruction(inst_file)
    simulator.init_memory(data_file)
    simulator.run(timeout_cycles)
    simulator.report(report_file)


if __name__ == '__main__':
    main()
