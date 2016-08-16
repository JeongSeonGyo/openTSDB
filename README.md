# openTSDB

설치 환경
 - Ubuntu 14.04, 32-bit

필요한 프로그램
 - Hadoop 2.6.4
 - Hbase 0.98.20
 - GnuPlot

1. GnuPlot
  * openTSDB에서 그래프 그릴 때 사용된다.

 1) 설치
    > gnuplot 홈페이지에서 다운
    
    	$ tar -xzvf gnuplot-x.x.x.tar.gz
    	$ cd gnuplot-x.x.x
    	$ ./configure
		$ make
    	$ make check
		$ make install
        
2. Hadoop
  
  1) 설치
    
    	$ cd /usr/local
		$ Hadoop 홈페이지에서 다운로드
		$ wget http://mirror.navercorp.com/apache/hadoop/common/hadoop-2.6.4/hadoop-2.6.4.tar.gz
		$ tar -xzvf hadoop-2.6.4
		$ sudo mkdir hadoop
		$ sudo mv hadoop-2.6.4/* hadoop/
	
   

  2) 실행
  
	# cd /usr/local/hadoop/sbin
	# ./start-all.sh
    	
    
  3) web ui 확인
   	> http://localhost:50070
    
3. HBase

  1) 설치
  
		# cd /usr/local/
		Hbase 홈페이지에서 0.98.20 릴리즈 파일을 다운로드 한다.
		# wget http://apache.mirror.cdnetworks.com/hbase/0.98.20/hbase-0.98.20-hadoop2-bin.tar.gz
		# tar -xzvf hbase-0.98.20-hadoop2-gin.tar.gz
		# mkdir hbase
		# mv hbase-0.98.29/* hbase/


  2) 속성 변경
  
    - JAVA_HOME : java 디렉토리
    - HBASE_MANAGES_ZK : hbase가 내장 zookeeper를 사용할 지 여부 (true : 내장 zookeeper 사용)
    		
    		# cd /usr/local/hbase/conf
    		# vim hbase-env.sh
    		export JAVA_HOME = /usr
    		export HBASE_MANAGES_ZK=true
    
    		# vim hbase-site.xml
		    <configuration>
		
			<property>
				<name>hbase.rootdir</name>
				<value>hdfs://localhost:9000/hbase</value>
			</property>
		
			<property>
				<name>hbase.zookeeper.quorum</name>
				<value>localhost</value>
			</property>
		
		
			<property> <name>hbase.zookeeper.property.dataDir</name> 
				<value>/home/hadoop/zookeeper</value> 
			</property>
		
			<property> 
				<name>hbase.cluster.distributed</name>
				 <value>true</value> 
			</property>
		
			<property>
		                <name>hbase.master.info.port</name>
		                <value>60010</value>
		    	</property>
			 <property>
		            <name>hbase.master.info.bindAddress</name>
		            <value>localhost</value>
			 </property>
			 <property>
		            <name>dfs.support.append</name>
		            <value>true</value>
			 </property>
			  <property>
		            <name>dfs.datanode.max.xcievers</name>
		            <value>4096</value>
			 </property>
			  <property>
		            <name>hbase.zookeeper.property.clientPort</name>
		            <value>2181</value>
			  </property>
			  <property>
		            <name>hbase.regionserver.info.bindAddress</name>
		            <value>localhost</value>
			 </property>
		    </configuration>

  3) hbase 실행
  
      
    	# cd /usr/local/hbase/bin
    	# ./start-hbase.sh
    	hbase shell 을 통해 hbase에 연결되었는지 확인
    	# hbase shell
    	~
    	>hbase(main):001:0> 
    
    
  4) hbase 종료
  
    	# ./stop-hbase.sh
    
    
  5) web ui 확인
    	> http://localhost:16010

4. openTSDB 

  1) 설치
  
    	# cd /usr/local/
    	# git clone git://github.com/OpenTSDB/opentsdb.git
    	# cd opentsdb
    	# ./build.sh
    

 2) 속성 변경
 
 
    	# cd /usr/local/opentsdb/src/ or /etc/
    - tsd.network.port = TSD 연결 포트
    - tsd.http.staticroot = OpenTSDB 홈페이지 파일 위치
    - tsd.http.cachedir = TSD 임시 파일 저장 위치
    - tsd.core.auto_create_metrics : true = 레코드의 metric이 데이터베이스에 존재하지 않을 때, 자동으로 metric 추가
    - tsd.storage.fix_duplicates : true = 같은 시간에 중복된 데이터가 존재하는 경우 마지막 입력된 데이터만 쓰임
    
	    	# vim opentsdb.conf
	    	tsd.network.port = 4242
	    	tsd.http.staticroot = /usr/share/opentsdb/static/
	    	tsd.http.cachedir = /usr/share/opentsdb/static/
   
    * logback.xml 파일을 수정하는 경우도 있지만 root 권한으로 openTSDB를 실행할 것이기 때문에 수정하지 않음
    
    
  3) 데이터베이스 테이블 구성 (최초로 한 번만 해준다)
  
  
	    # env COMPRESSION=NONE HBASE_HOME=path/to/hbase-0.94.X ./src/create_table.sh
	    # tsdtmp=${TMPDIR-'/tmp'}/tsd
	    # mkdir -p "$tsdtmp"
	    # ./build/tsdb tsd --port=4242 --staticroot=build/staticroot --cachedir="$tsdtmp" --zkquorum=myhost:2181
    
    
	    ~
	    create 'tsdb-uid'
	    create 'tsdb'
	    create 'tsdb-tree'
	    create 'tsdb-meta'
	    가 생성되면 됨
    
    
  4) openTSDB 실행
  
    > Hadoop 실행 -> hbase 실행 -> openTSDB 실행
    
