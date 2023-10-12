from bsquant.rolling_optimize_cta_backtester import RollingOptimizeCtaBacktester
from bsquant.base_cta_strategy import BaseCtaStrategy


def run():
    ro_engine = RollingOptimizeCtaBacktester()
    strategy = BaseCtaStrategy()
    ro_engine.add_strategy(strategy)

    result = ro_engine.run()



if __name__ == '__main__':
    run()
