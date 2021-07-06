import logging

logging.basicConfig(filename=r'src\test\test_log.log', encoding='utf-8', format='%(asctime)s %(message)s', datefmt="%Y-%m-%d %I:%M:%S", level=logging.INFO)

trial_number=3
num_trials=5
elapsed=3.21435
n=100
d=10
eta=0.9
M=5
data_filepath="aah"
rows=range(10)
columns=range(5)

msg = (
        "Finished trial {0}/{1}, ".format(trial_number, num_trials) +
        "elapsed={}, ".format(elapsed) +
        "n={0}, d={1}, eta={2}, M={3}, ".format(n,d,eta,M) +
        "data={0}, rows={1}, columns={2} ".format(data_filepath, rows, columns)
    )
logging.info(msg)