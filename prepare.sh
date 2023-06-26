S1="1uoAReQK3f5g9CEy8rV4haSzXll8NqVHW";
S2="gfm-models.zip";
CONFIRM=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate "https://drive.google.com/uc?export=download&id=$S1" -O- | sed -En 's/.*confirm=([0-9A-Za-z_]+).*/\1/p');
wget --load-cookies /tmp/cookies.txt "https://drive.google.com/uc?export=download&confirm=$CONFIRM&id=$S1" -O $S2;
rm -f /tmp/cookies.txt
unzip gfm-models.zip