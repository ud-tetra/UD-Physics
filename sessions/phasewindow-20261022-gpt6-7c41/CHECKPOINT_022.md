# Checkpoint symmetry-moving-022

STATUS: NUMERICAL/DEVELOPMENT; exact A5 representation imported from checkpoints 020–021, no new independent physical prediction.

Main verified read-only SHA: 7834e6407778e5b6c2c2bacd27eb64c13687a172. Held claim task icosahedral-phasewindow-20261022 session phasewindow-20261022-gpt6-7c41; branch 7edcc4987525b26c7f9f42925368aea5c7a91874 before this checkpoint. Other held greenbounds PR44 untouched.

Completed: six-output full560 tangent adjoint for 11 selected times 1–100, uniform symmetric baseline, beta=.005 nu=.05 cf=0, Eh<=51/20000000. Peak 6.6002751368e-05 at u=4; u100 values 4.260936553e-06, 4.2442760579e-06. 24-output cross-check u4 rel 4.84e-08; 2-dir forward transpose u4 rel 3.08e-07; latter at u100 TIMEOUT.

Not completed: rigorously validated ODE integration, continuous-time envelope, nonlinear second-order remainder all phase directions, positive 120 housing struts for arbitrary housing phases to u100, scattered qualified property box. This package is an executable local capture and SHA256 manifest; no mainline writeback.

Next: robust u100 adjoint validation via stable block/interval integrator and coupled nonlinear bootstrap; avoid marginal short tubes.