deps:
    FROM ubuntu:20.10
    RUN apt-get update && apt-get install -y python3 python3-pip git
    RUN pip3 install matplotlib pandas pywaffle

code:
    FROM +deps
    WORKDIR /dontusepiecharts
    COPY --dir data .
    COPY --dir dontusepiecharts .
    ARG pad_inches="0"
    ENV NOPIE_pad_inches="$pad_inches"

plot-random:
    FROM +code
    RUN python3 dontusepiecharts/plotrandom.py
    SAVE ARTIFACT *.png AS LOCAL ./output/

plot-precipitation:
    FROM +code
    RUN python3 dontusepiecharts/plotprecipitation.py
    SAVE ARTIFACT *.png AS LOCAL ./output/

plot-pacman:
    FROM +code
    RUN python3 dontusepiecharts/pacman.py
    SAVE ARTIFACT *.png AS LOCAL ./output/

plot:
    ARG pad_inches="0"
    BUILD +plot-random --pad_inches="$pad_inches"
    BUILD +plot-precipitation --pad_inches="$pad_inches"
    BUILD +plot-pacman --pad_inches="$pad_inches"

plot-with-padding:
    BUILD +plot --pad_inches="4"
