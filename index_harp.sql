use jcmt;
select qa.utdate, qa.obsnum, qb.subsysnr, qb.subbands, qc.file_id, qa.instrume, qa.obs_type from COMMON as qa 
left join ACSIS as qb on (qa.obsid=qb.obsid) right join FILES as qc on (qa.obsid=qc.obsid)
where qa.instrume='HARP' and qa.utdate between 20190423 and 20190430 and obs_type='science';


