# FengYun-2 S-VISSR Sync + Counter Corrector
This is a simple program for fixing S-VISSR transport frames of FengYun-2 satellites. This allows you to get a good photo with a bad SNR together with [SatDump](https://github.com/altillimity/SatDump)

![1](https://github.com/Foxiks/fengyun2-svissr-corrector/blob/main/img/L7K7Csk2SLu09Q4bpgr11X1s4ta3TBXVkw467q7uRuVjBA9lPi8C4ZuoOD8vIyd8RwqZAk7zwVAMm-7uYim4ZgET.jpg)

## Using
At the moment, the corrector works well only with data for a full transmission session! Start recording 1-2 minutes before the transmission starts and stop recording after the transmission ends. Otherwise, the corrector may give a bad result. I will fix this issue soon...
1. Place the FengYun-2_corrector.json file from the Pipelines folder of this repository into the Pipelines folder in the satdump folder.
2. Start transport frame decoding via FengYun-2 S-VISSR (Egor UB1QBJ Sync + Counter Corrector). This will save the transport frames to the Live_output folder in the Satdump folder. (if you did not change this folder in the settings)

![2](https://github.com/Foxiks/fengyun2-svissr-corrector/blob/main/img/P3jhZyqw7l-vIi_2wW14ZHgIH3GLphM5gEunAHK4kNoC3D3NAC6xynafrvoRc4mRlTRvFmT_y2roXFOqzOcHEQYu.jpg)
3. After receiving the file with S-VISSR transport frames, use the corrector. For Windows, you can use a simple launcher in the corrector folder. Otherwise, use this style of command to run:
```sh
FengYun2-Counter-Corrector.exe -i (--input) input_file.bin (fengyun_svissr.svissr) -o --output (fengyun_svissr.svissrcorrected)
```
or
```sh
python FengYun2-Counter-Corrector.py -i (--input) input_file.bin (fengyun_svissr.svissr) -o --output (fengyun_svissr.svissrcorrected)
```
Note! There must be no spaces in the paths to the input and output files!

4. Open the received corrected data in Satdump with the parameters as in the screenshot:
![3](https://github.com/Foxiks/fengyun2-svissr-corrector/blob/main/img/DpIzr5mFOv9PsIhnjiyQwjt8lxXKys1vM2exDWWAe93aRFug6--KaSk8Fsim6wUj9jXPT48WCyTLZUtt0PP8Ah8Q.jpg)
5. Get a good picture with a bad SNR!
![4](https://github.com/Foxiks/fengyun2-svissr-corrector/blob/main/img/DqEH9Ok0juNNhw9HQo_AkmHX_snfyveqMLoegxV0aV-RjIq0KsXOzVMyIVgJzYAy0G_Hwb_PE6eAoMDwy3KLOyEh.jpg)
