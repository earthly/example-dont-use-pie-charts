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

#plot-earthly-blog-hacks:
#    # the earthly blog image processor fails on small images
#    # to hack around this, I had to include margin padding and increase the font size
#    BUILD +plot --pad_inches="4" --font_size="20"

cv2-deps:
    FROM +deps
    RUN apt-get install ffmpeg libsm6 libxext6  -y
    RUN pip3 install opencv-python

resize-images:
    FROM +cv2-deps
    COPY output/*.png .
    COPY resize-images-hack.py .

    RUN python3 resize-images-hack.py --width=1100 --height=400 bar-chart.png
    RUN python3 resize-images-hack.py --width=1300 --height=1000 pie-chart.png
    RUN python3 resize-images-hack.py --width=1300 --height=1000 rainfall-by-day-of-week-pie-chart-is-hard-to-read.png

    #RUN python3 resize-images-hack.py --width=1 --height=1 distribution-of-days-that-experience-rain.png
    #RUN python3 resize-images-hack.py --width=1 --height=1 distribution-of-days-that-experience-rain-waffle-chart.png
    #RUN python3 resize-images-hack.py --width=1 --height=1 horizontal-bar-chart.png
    #RUN python3 resize-images-hack.py --width=1 --height=1 horizontal-lollipop-chart.png
    #RUN python3 resize-images-hack.py --width=1 --height=1 pacman.png
    #RUN python3 resize-images-hack.py --width=1 --height=1 rainfall-by-day-of-week-box-and-whisker.png
    #RUN python3 resize-images-hack.py --width=1 --height=1 rainfall-by-day-of-week-box-and-whisker-when-raining.png
    #RUN python3 resize-images-hack.py --width=1 --height=1 rainfall-by-day-of-week-box-and-whisker-with-outliers.png
    #RUN python3 resize-images-hack.py --width=1 --height=1 rainfall-by-day-of-week.png



    SAVE ARTIFACT *.png AS LOCAL ./output-resized/
