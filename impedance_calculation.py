import math
import matplotlib.pyplot as plt
import pandas as pd

supply = 1
start_frequency = 1 * 10**3
stop_frequency = 100 * 10**3

r = 2 * 10**-3
d_ed = 0.25 * 10**-3
d_sc = 0.02 * 10**-6

# # normal
# sigma_sc = 0.07
# sigma_ed = 2.60
# e_r_sc = 1.25 * 10**6
# e_r_ed = 4.67 * 10**7
# e_o = 8.854 * 10**-12

# cancer
sigma_sc_c = 2.94
sigma_ed_c = 2.94
e_r_sc_c = 52898628.95
e_r_ed_c = 52898628.95

# form paper
sigma_sc = 5 * 10**-5
sigma_ed = 0.02
e_r_sc = 2.0 * 10**3
e_r_ed = 2.0 * 10**5
e_o = 8.854 * 10**-12


area = math.pi*r**2

# normal
R_1 = d_sc/(sigma_sc*area)
R_2 = d_ed/(sigma_ed*area)
C_1 = (e_o * e_r_sc*area)/d_sc
C_2 = (e_o * e_r_ed*area)/d_ed


# cancer
R_1_c = d_sc/(sigma_sc_c*area)
R_2_c = d_ed/(sigma_ed_c*area)
C_1_c = (e_o * e_r_sc_c*area)/d_sc
C_2_c = (e_o * e_r_ed_c*area)/d_ed


freq_list = []
impedance_list_2 = []
impedance_list = []
for f in range(start_frequency, stop_frequency):
    z = (2 * R_1)/complex(1, 2*math.pi*f * R_1 * C_1)+(3 * R_2)/complex(1, 2*math.pi*f * R_2 * C_2)
    z_c = (2 * R_1_c) / complex(1, 2 * math.pi * f * R_1_c * C_1_c) + (3 * R_2) / complex(1, 2 * math.pi * f * R_2_c * C_2_c)
    freq_list.append(f)
    impedance_list.append(abs(z))
    impedance_list_2.append(abs(z_c))

data = {'frequency': freq_list, 'Impedance': impedance_list, 'Impedance_2': impedance_list_2}
df = pd.DataFrame(data).to_csv('impedance_data.csv', index=None)
# print data
plt.plot(freq_list[start_frequency:stop_frequency], impedance_list[start_frequency:stop_frequency], color='red', label= 'Non-Cancerous')
plt.plot(freq_list[start_frequency:stop_frequency], impedance_list_2[start_frequency:stop_frequency], color='green', label='Cancerous')
plt.legend()
plt.grid()
plt.show()
