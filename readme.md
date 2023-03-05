## 설명

- single shard test 를 위한 커스텀 트랙입니다.
- 데이터 출처인 wordList.txt 는 용량 문제로 업로드 하지 않습니다. 
- wordList.txt 의 데이터는 https://ko-nlp.github.io/Korpora/ko-docs/corpuslist/kowikitext.html 의 데이터의 단어를 단어의 set 으로 만든 자료로 대체가 가능합니다.


### wordList.txt
실제 환경에서는 600 MB 의 겹치지 않은 단어의 모음 파일을 사용했습니다. 실제 테스트에서는 실제 쓰는 데이터를 사용하는 해야 올바른 테스트를 수행가능합니다.
해당 파일은 github 크기 문제로 업로드 하지 않으나, 테스트 환경을 구성하기위한 데이터 소스 링크를 남깁니다.

- https://ko-nlp.github.io/Korpora/ko-docs/corpuslist/kowikitext.html

### SST_insert 
단어의 크기 별 insert 를 위한 트랙입니다.

1. 실행 전 해당 경로에서 python toJSON.py 를 실행하여 테스트 환경을 만듭니다. document.json , corpora.json 이 만들어지면 실행 가능합니다.
2. 실행 커맨드
```
esrally race --pipeline=benchmark-only --track-path={track_path} --target-host={es_uri}
```

### SST_searchOps
search operation 에 대한 테스트 트랙입니다.

1. 위의 각 스텝에 대해 단계적으로 진행하면서 병목 지점을 찾습니다.
2. 프로젝트 디렉토리에 wordList.txt 가 제대로 존재함을 확인합니다.
```
esrally race --pipeline=benchmark-only --track-path={track_path} --target-host={es_uri} ----track-params=target-throughput:{my_target_throughput}
```
3. 위의 target througput 은 100, 200,400,800, 1500 으로 순차적으로 늘려갑니다. (하드웨어나 쿼리 상황에 따라 다른 값을 사용합시다.)