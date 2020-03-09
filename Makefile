comptest_package=zuper_nodes_tests,zuper_nodes_wrapper_tests
out=out-comptests
coverage_dir=out-coverage
coverage_include='*src/zuper_*'
coveralls_repo_token=JJ8Zi6WCBp6p09pCLuMp9fyfD88Rq2BpW

test:
	docker-compose down -v
	docker-compose up --build  -V --abort-on-container-exit

bump-upload:
	$(MAKE) bump
	$(MAKE) upload

bump:
	bumpversion patch

upload:
	git push --tags
	git push
	rm -f dist/*
	rm -f src/*.egg-info
	python2 setup.py sdist
	twine upload dist/*

