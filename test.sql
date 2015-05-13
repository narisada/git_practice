/*sqlite3のコマンドバッチファイル（テストver）*/

.headers ON --カラム名を表示
.show　--現在の設定


/*create table文*/
create table test(birdid integer,birdname text, primary key(birdname,birdid);
/*CREATE TABLE テーブル名(カラム名1 データ型, カラム名2 データ型, ...)*/
/*PRIMARY KEY:カラムに重複した値を格納できない */


/*alter table 文:テーブル名の変更・カラムの追加*/
alter table test rename to birds;
alter table birds add column birdtype text;
/*PRIMARY KEY・UNIQUE制約不可*/


/*drop table文・vacuum文*/
/*
drop table test;
vacuum;
*/


/*insert into 文*/
/*insert into birds(birdid, birdname, birdtype) values(1, 'ヒヨドリ','留鳥');*/
insert into test(birdid, birdname) values(1, 'ヒヨドリ');


/*select文*/
select * from sqlite_master;
/*テーブル構造の確認: |タイプ|名前|テーブル名|ルートページ|CREATE TABLE文|*/

select * from sqlite_master where type='table' and name='C';





select * from birds;
select * from test;

select * from sqlite_master where type='view';
