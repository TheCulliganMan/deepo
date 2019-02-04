build:
		$(MAKE) clean
		python ./scripts/make-gen-docker.py
		bash ./scripts/gen-docker.sh
		python ./scripts/make-circleci.py

clean:
		rm -rf ./scripts/gen-docker.sh || true
		rm -rf ./docker/* || true
		rm -rf ./circle.yml || true