# These targets are not files
.PHONY: contribute test syncdb requirements static

all: env/ var/

install: requirements static
	. env/bin/activate && python setup.py develop
	. env/bin/activate && python manage.py syncdb --migrate

static:
	mkdir -p public/static/

	. env/bin/activate && python manage.py collectstatic \
	         -v 0 \
	         --noinput \
	         --traceback \
	         -i django_extensions
	
	find public/static/ -type f -not -name '*.gz' | xargs -I name sh -c 'gzip --best < name > name.gz'

virtualenv.py:
	wget -c https://raw.github.com/pypa/virtualenv/develop/virtualenv.py

requirements:
	. env/bin/activate && pip install -r requirements/development.txt
	. env/bin/activate && pip install -r requirements/production.txt

env/: virtualenv.py
	python virtualenv.py --prompt="(env)" env

var/:
	mkdir -p var/log
	mkdir -p var/cache
	mkdir -p var/run

test:
	./runtests.py tests/

clean:
	rm -r var/log/*
	rm -r var/cache/*
	rm -r var/run/*	
	rm -r public/static/*

fullclean: clean
	rm -r env/
	rm -r virtualenv.py
