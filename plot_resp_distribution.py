import os
import numpy as np
import matplotlib.pyplot as plt 

import  scipy.stats


import respirationtools
import neo



def analyse_dir(dirname, debug=False):
    
    resp_sig = np.memmap(os.path.join(dirname, 'input0.raw'), dtype='float32')
    print(resp_sig.shape)
    
    # TODO read sample rate form file
    sr = 1000.
    t_start = 0.
    
    analyse_resp(resp_sig, sr, t_start)


def analyse_trc(trc_filename, channel_name):
    
    reader = neo.MicromedIO(filename=trc_filename)
    seg = reader.read_segment()
    
    channel_ind = None
    for anasig in seg.analogsignals:
        #~ print()
        #~ print(anasig.shape)
        if channel_name in anasig.array_annotations['channel_names']:
            channel_ind = anasig.array_annotations['channel_names'].tolist().index(channel_name)
            resp_sig = anasig[:, channel_ind].magnitude.flatten()
            sr = anasig.sampling_rate.rescale('Hz').magnitude
            t_start = 0.
            break
    
    print('channel_ind', channel_ind)
    if channel_ind is None:
        raise(Exception('Channel not found'))
    
    #~ fig, ax = plt.subplots()
    #~ ax.plot(resp_sig)
    #~ plt.show()
    analyse_resp(resp_sig, sr, t_start)


def analyse_resp(resp_sig, sr, t_start):
    
    #~ print('compute cycles')
    cycle_indexes = respirationtools.detect_respiration_cycles(resp_sig, sr, t_start=t_start, output = 'index',
                                                    inspiration_sign = '-',
                                                    # baseline
                                                    #~ baseline_with_average = False,
                                                    baseline_with_average = True,
                                                    manual_baseline = 0.,

                                                    high_pass_filter = None,
                                                    constrain_frequency = None,
                                                    median_windows_filter = None,

                                                    # clean
                                                    eliminate_time_shortest_ratio = 8,
                                                    eliminate_amplitude_shortest_ratio = 4,
                                                    eliminate_mode = 'OR', ) # 'AND')
    #~ print(cycle_indexes)
    
    resp_sig2 = resp_sig.copy()
    resp_sig2 -=np.mean(resp_sig2)
    resp_features = respirationtools.get_all_respiration_features(resp_sig2, sr, cycle_indexes, t_start = 0.)
    print(resp_features.columns)
    
    
    cycle_amplitudes = resp_features['total_amplitude'].values
    
    
    # figure 1
    fig0, axs = plt.subplots(nrows=3, sharex=True)
    
    
    times = np.arange(resp_sig.size)/sr
    
    #~ axs[0].set_title(os.path.basename(dirname))
    
    # ax0
    ax = axs[0]
    ax.plot(times, resp_sig)
    ax.plot(times[cycle_indexes[:, 0]], resp_sig[cycle_indexes[:, 0]], ls='None', marker='o', color='r')
    ax.plot(times[cycle_indexes[:, 1]], resp_sig[cycle_indexes[:, 1]], ls='None', marker='o', color='g')
    ax.set_xlim(0,120)
    ax.set_ylabel('resp')
    
    cycle_durations = np.diff(cycle_indexes[:, 0])/sr
    cycle_freq = 1./cycle_durations

    # ax1
    ax = axs[1]
    ax.plot(times[cycle_indexes[:-1, 0]], cycle_freq)
    ax.set_ylim(0, max(cycle_freq)*1.1)
    ax.axhline(np.mean(cycle_freq), color='m')
    ax.axhline(np.median(cycle_freq), color='m', linestyle='--')
    ax.set_ylabel('freq')

    # ax2
    ax = axs[2]
    ax.plot(times[cycle_indexes[:-1, 0]], cycle_amplitudes)
    ax.set_ylabel('amplitude')

    title2 = 'mean={:0.3f}'.format(np.mean(cycle_amplitudes))
    
    axs[0].set_title(title2)
    
    #Figure 2

    fig1, axs = plt.subplots(nrows=2)

    # ax0
    ax = axs[0]
    count, bins = np.histogram(cycle_freq, bins=np.arange(0,1.5,0.01))
    ax.plot(bins[:-1], count)
    ax.set_xlabel('freq (Hz)')
    
     #~ print(bins, count)
    
    
    ax.axvline(np.mean(cycle_freq), color='m')
    ax.axvline(np.median(cycle_freq), color='m', linestyle='--')
    
    W, pval = scipy.stats.shapiro(cycle_freq)
    
    
    title = 'mean={:0.3f}  median={:0.3f} W={:0.3f} pval={:0.5f}'.format(np.mean(cycle_freq), np.median(cycle_freq), W, pval)
    axs[0].set_title(title)
    
    

    
    # ax1    resp_sig = np.memmap(os.path.join(dirname, 'input0.raw'), dtype='float32')
    print(resp_sig.shape)
    
    # TODO read sample rate form file
    sr = 1000.
    t_start = 0.
    

    ax = axs[1]
    ratio = (cycle_indexes[:-1, 1] - cycle_indexes[:-1, 0]).astype('float64') / (cycle_indexes[1:, 0] - cycle_indexes[:-1, 0])
    count, bins = np.histogram(ratio, bins=np.arange(0, 1., 0.01))
    ax.plot(bins[:-1], count)
    ax.set_xlabel('ratio ')
    ax.set_ylabel('ratio = {:.3f}'.format(np.mean(ratio)))
    
    ###ici affichage des donnees parametres sur l invite de commande
    #~ print(ratio)
    #~ print(np.mean(ratio), np.std(ratio))
    #~ print ('zozo on passe de ratio a freq')
    #~ print(cycle_freq)
    #~ print('moy freq', np.mean(cycle_freq), 'std freq', np.std(cycle_freq))

    ###ici legendes axes
    
    
    print(count)
    
    
    
    return [fig0, fig1]
    
    
    
    
    
    
    
        #~ # compute resp features
    #~ print('compute features')
    #~ resp_features = respirationtools.get_all_respiration_features(resp_sig, sr, cycle_indexes, t_start=t_start)
    
    #~ return resp_features






if __name__ == '__main__':

    #~ dirname = '/home/samuel/Pre_manip_respi_driver/2018-11-21T13h56m09_subject=_phase=freeResp'
    #~ dirname = 'C:/Users/manip/Pre_manip_respi_driver/2018-11-22T11h03m45_subject=_phase=freeResp'
    
    
    #~ dirname = '/home/samuel/mnt/CRNLDATA/crnldata/cmo/Partage/NBuonviso201810_ieeg_respi_jules/DataPreManip/2018-11-22T11h34m23_subject=nath1_phase=drivenResp'
    
    #~ dirname = 'C:/Users/manip/Pre_manip_respi_driver/2019-01-08T16h54m22_subject=Jules_phase=freeResp'
    
    #~ dirname = 'C:/Users/manip/Pre_manip_respi_driver/2019-01-10T10h39m34_subject=Emmanuelle Rampe_phase=drivenResp'
    #~ dirname = 'C:/Users/manip/Pre_manip_respi_driver/2019-01-09T11h02m10_subject=_phase=freeResp'
    #~ analyse_dir(dirname, debug=True)
    
    
    ##### channel name correspond a la voie de la respiration NASALE et le TRC a la periode de repos de 3 min en free resp
    #~ trc_filename = 'EEG_7095.TRC'
    #~ channel_name = 'p7+'
    
    #~ analyse_trc(trc_filename, channel_name)

    ##### channel name correspond a la voie de la respiration NASALE et le TRC a la periode de repos de 3 min en free resp
    # patient PAPp
    trc_filename = 'EEG_44576.TRC'
    channel_name = 'p19+'
    
    analyse_trc(trc_filename, channel_name)
    
    
    plt.show()



    