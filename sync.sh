rsync -avz ./ pi@192.168.0.30:/home/pi/escpos2

ssh rpi 'cd escpos2 && pip install . --upgrade'
ssh rpi 'sudo systemctl restart todo'
