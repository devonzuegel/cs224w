#should be 45
import snap
import matplotlib.pyplot as plt

THRESHOLDS_FILE = './data/thresholds.txt'
PLOT_TITLE      = 'Cumulative Thresholds'
PLOT_RANGE      = [0, 100]

def get_histogram():
  histogram = []
  with open(THRESHOLDS_FILE) as f:          histogram = f.read().splitlines()
  for i in range(0, len(histogram) - 1):    histogram[i] = int(histogram[i])
  return histogram

def get_cumulative_histogram(histogram):
  cum_hist    = [0] * len(histogram)
  cum_hist[0] = histogram[0]
  for i in range(1, len(histogram) - 1):
    cum_hist[i] += histogram[i] + cum_hist[i - 1]
  return cum_hist

def get_total_n_rioters(cum_hist):
  total_n_rioters = 0

  for i in range(0, len(cum_hist) - 1):
    beyond_threshold = (i == 0 or cum_hist[i - 1] >= i)
    if beyond_threshold:   total_n_rioters += histogram[i]
    else:                  break

  return total_n_rioters

histogram       = get_histogram()
cum_hist        = get_cumulative_histogram(histogram)
total_n_rioters = get_total_n_rioters(cum_hist)

print 'Cumulative total # of rioters would be:', total_n_rioters

# Create histogram.
plt.title(PLOT_TITLE)
plt.xlim(PLOT_RANGE)
plt.ylim(PLOT_RANGE)
plt.hist(cum_hist, len(cum_hist), cumulative = True)

# Save histogram to file.
plt.savefig('./images/1c-cumulative-histogram.png')