import argparse
from itertools import accumulate, chain, repeat

import numpy as np
import numpy.typing as npt


def create_egg(sample_rate: int, open_quotient: float, duration: float) -> npt.NDArray:
    t0 = sample_rate * duration * 1e-3
    d = round(open_quotient * t0)
    a = 27 / (4 * t0 * open_quotient**2)
    b = 27 / (4 * t0**2 * open_quotient**3)
    dv = (2 * a * i - 3 * b * i**2 for i in range(0, d))
    dv = chain(dv, repeat(0, round(t0) - d))
    ir = np.array(list(accumulate(dv)))
    return ir / np.sqrt(np.mean(ir * ir))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--samplerate", type=int, default=44100)
    parser.add_argument("-q", "--quotient", type=float, default=0.2)
    parser.add_argument("-d", "--duration", type=float, default=100)
    args = parser.parse_args()

    egg = create_egg(args.samplerate, args.quotient, args.duration)
    print(",".join((str(x) for x in egg)))
