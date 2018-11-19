rsync -avz ./ pi@192.168.0.30:/home/pi/escpos

ssh rpi 'cd escpos && pip install . '
ssh rpi 'sudo systemctl restart todo'
