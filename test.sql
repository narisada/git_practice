/*sqlite3のコマンドバッチファイル（テストver）*/
/*コマンド　sqlite3 sample.db < test.sql */
.headers ON --カラム名を表示
.show　--現在の設定


/*create table文*/
/*
create table birds(birdid integer,birdname text, primary key(birdname,birdid));
*/

create table birdslog(act text);


/*CREATE TABLE テーブル名(カラム名1 データ型, カラム名2 データ型, ...)*/
/*PRIMARY KEY:カラムに重複した値を格納できない */




/*alter table 文:テーブル名の変更・カラムの追加*/
/* 
alter table test rename to birds;
*/
/*
alter table birds add column birdtype text;
alter table birds add column BP integer;
*/
/*PRIMARY KEY・UNIQUE制約不可*/


/*drop table文・vacuum文*/
/*
drop table test;
vacuum;
*/
/*
drop table birds;
vacuum;
*/


/*insert into 文*/
/*insert into birds(birdid, birdname, birdtype) values(1, 'ヒヨドリ','留鳥');*/
/*insert into test(birdid, birdname) values(1, 'ヒヨドリ');
*/
/*
insert into birds(birdid, birdname, birdtype, BP) values(1, 'ヒヨドリ','留鳥',10);
insert into birds(birdid, birdname, birdtype, BP) values(2, 'スズメ','留鳥',5);
insert into birds(birdid, birdname, birdtype, BP) values(3, 'シジュウカラ','留鳥',20);
insert into birds(birdid, birdname, birdtype, BP) values(4, 'ヤマガラ','留鳥',50);
insert into birds(birdid, birdname, birdtype, BP) values(5, 'トビ','留鳥',25);
*/
/*
insert into birds(birdid, birdname, birdtype, BP) values(6, 'コルリ','夏鳥',600);
*/

/*select文*/
select * from sqlite_master;
/*テーブル構造の確認: |タイプ|名前|テーブル名|ルートページ|CREATE TABLE文|*/

select * from sqlite_master where type='table' and name='C';


/*CREATE INDEX　文*/
/*
create index idxBirds on birds(birdname);
*/
/*CREATE INDEX インデックス名 ON テーブル名(カラム名1, カラム名2, );*/


/*Trigger*/
/*create trigger 文*/
/*
create trigger trigBirds after insert on birds
begin 
      insert into birdslog(act) values('INSERT action');
end;

*/
/*
CREATE TRIGGER トリガー名 [ BEFORE | AFTER | INSTEAD OF]
 { DELETE | UPDATE [OF カラム名, ...] | INSERT } ON テーブル名
 [ FOR EACH ROW | FOR EACH STATEMENT ]
 [ WHERE 条件式 ]
 BEGIN
  SQL文1;
  SQL文2;
  ...
 END;
*/


select * from birds;
select * from birdslog;
/* select * from test; */

select * from sqlite_master where type='view';

/* .indicesコマンド：indexをすべて表示*/
/*
.indices
*/

