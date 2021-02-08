IMG ?= "pod-stress"
PORT ?= 5000

PRIMARY_IP := ""
RUN_MSG := "Access the API for pod-stress at http://localhost:${PORT}"
UNAME_S := $(shell uname -s)

ifeq ($(UNAME_S),Darwin)
	PRIMARY_IP := $(shell ipconfig getifaddr en0)
else ifeq ($(UNAME_S),Linux)
	PRIMARY_IP := $(shell ip route get 8.8.8.8 | head -1 | cut -d' ' -f7)
endif

ifneq ("$(PRIMARY_IP)","")
	RUN_MSG += "or http://${PRIMARY_IP}:${PORT}"
endif

build:
	docker build . -t ${IMG}

run: build
	@echo "\n\n${RUN_MSG}"
	@docker run -p ${PORT}:5000 ${IMG}