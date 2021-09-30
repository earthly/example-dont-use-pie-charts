deps:
    FROM ubuntu:20.10
    RUN apt-get update && apt-get install -y python3 python3-pip git
    RUN pip3 install matplotlib pandas pywaffle

code:
    FROM +deps
    WORKDIR /dontusepiecharts
    COPY --dir data .
    COPY --dir dontusepiecharts .

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
    BUILD +plot-random
    BUILD +plot-precipitation
    BUILD +plot-pacman
