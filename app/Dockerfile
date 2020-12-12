 FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y \
	libopencv-dev \
        python3-pip \
	python3-opencv && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install numpy pandas sklearn matplotlib jupyter && \
    pip3 install opencv-python && \
    pip3 install imutils && \
    pip3 install flask

RUN ["mkdir", "app"]

WORKDIR /app

RUN ["mkdir", "uploaded_images"]
RUN ["mkdir", "patched_images"]
RUN ["mkdir", "images_classified"]
RUN ["mkdir", "csv_files"]
RUN ["mkdir", "csv_classifications"]

COPY ./src ./

EXPOSE 5000

CMD ["python3","App.py"]