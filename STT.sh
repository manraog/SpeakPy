arecord -D plughw:1,0 -q -f cd -t wav -d 4 -r 16000 | flac - -f --best --sample-rate 16000 -s -o voz.flac;
 
wget -q -U "Mozilla/5.0" --post-file voz.flac --header "Content-Type: audio/x-flac; rate=16000" -O - "http://www.google.com.mx/speech-api/v2/recognize?output=json&lang=es&key=AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw" | cut -d\" -f8  > stt.txt
 
value=`cat stt.txt`
echo "$value"