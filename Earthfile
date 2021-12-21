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
    ARG font_size=""
    ENV NOPIE_pad_inches="$pad_inches"
    ENV NOPIE_font_size="$font_size"

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
    ARG font_size=""
    BUILD +plot-random --pad_inches="$pad_inches" --font_size="$font_size"
    BUILD +plot-precipitation --pad_inches="$pad_inches" --font_size="$font_size"
    BUILD +plot-pacman --pad_inches="$pad_inches" --font_size="$font_size"

cv2-deps:
    FROM +deps
    RUN apt-get install ffmpeg libsm6 libxext6  -y
    RUN pip3 install opencv-python

resize-images:
    FROM +cv2-deps
    COPY output/*.png .
    COPY resize-images-hack.py .

    # These resizes are required to prevent jekyl from failing to format these images
    #   Jekyll Picture Tag Warning: /assets/images/stop-using-pie-charts/distribution-of-days-that-experience-rain-waffle-chart.png
    #   is 800px wide (after cropping, if applicable),
    #   smaller than at least one size in the set [400, 600, 800, 1000].
    #   Will not enlarge.
    # Ideally, I would rather jekyll would resize them, but it was not clear how to do this.

    RUN python3 resize-images-hack.py --width=1100 --height=400 bar-chart.png
    RUN python3 resize-images-hack.py --width=1300 --height=1000 pie-chart.png
    RUN python3 resize-images-hack.py --width=1300 --height=1000 rainfall-by-day-of-week-pie-chart-is-hard-to-read.png
    RUN python3 resize-images-hack.py --width=1000 --height=400 distribution-of-days-that-experience-rain-waffle-chart.png

    SAVE ARTIFACT *.png AS LOCAL ./output-resized/
