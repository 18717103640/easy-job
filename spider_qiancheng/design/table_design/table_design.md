
-- 1 条件表

CREATE TABLE IF NOT EXISTS `qiancheng_condition` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT COMMENT '主键id',
  `condition` varchar(255) DEFAULT NULL COMMENT '查询条件',
  `res_count` int DEFAULT NULL COMMENT 'resCount',
  `total_count` int DEFAULT NULL COMMENT '总数据量',
  `created_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `UK_condition` (`condition`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='qiancheng条件表';

-- 2 条件失败表
CREATE TABLE IF NOT EXISTS `qiancheng_condition_fail` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT COMMENT '主键id',
  `condition` varchar(255) NOT NULL COMMENT '查询条件',
  `retry_times` tinyint NOT NULL COMMENT '重试次数',
  `created_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `UK_condition` (`condition`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='qiancheng条件查询失败记录表';

-- 3 任务表

CREATE TABLE IF NOT EXISTS `qiancheng_task` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT COMMENT '主键id',
`task_id` bigint unsigned NOT NULL COMMENT '任务序列号',
`condition` varchar(255)  NULL DEFAULT NULL COMMENT '查询条件',
`status` tinyint NOT NULL DEFAULT '0' COMMENT '任务状态(0:未开始,1:正在进行;2:已完成)',
`current_page` tinyint NOT NULL COMMENT '当前分页数',
`page` tinyint NOT NULL COMMENT '总页数',
`order` int NOT NULL COMMENT '优先级',
`created_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
`updated_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
PRIMARY KEY (`id`) USING BTREE,
KEY `IDK_task_id_condition_status_page` (`task_id`,`condition`,`status`,`page`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET = utf8mb4 COMMENT='任务记录表';

-- 4 任务失败表
CREATE TABLE IF NOT EXISTS `qiancheng_task_fail` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT COMMENT '主键id',
`task_id` bigint unsigned NOT NULL COMMENT '任务序列号',
`condition` varchar(255)  NULL DEFAULT NULL COMMENT '查询条件',
`current_page` tinyint NOT NULL COMMENT '当前分页数',
`retry_time` tinyint NOT NULL COMMENT '重试次数',
`created_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
`updated_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
PRIMARY KEY (`id`) USING BTREE,
KEY `IDK_task_id_condition_page_retry_time` (`task_id`,`condition`,`current_page`,`retry_time`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET = utf8mb4 COMMENT='任务失败记录表';


-- 5 平台 job表
CREATE TABLE `qiancheng_job` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT COMMENT '主键id',
  `brand_name` varchar(255) NOT NULL COMMENT '公司名称',
  `job_name` varchar(255) NOT NULL COMMENT '岗位名称',
  `salary_desc_min` varchar(255) NULL DEFAULT NULL COMMENT '薪水最低',
  `salary_desc_max` varchar(255) NULL DEFAULT NULL   COMMENT '薪水最高',
  `salary_desc` varchar(255) NULL DEFAULT NULL   COMMENT '薪水',
  `city_name` varchar(255) NULL DEFAULT NULL COMMENT '城市',
  `area_district` varchar(255) NULL DEFAULT NULL COMMENT '区域',
  `business_district` varchar(255) NULL DEFAULT NULL COMMENT '街道',
  `location` varchar(255) NULL DEFAULT NULL COMMENT '地点(cityName+areaDistrict+brandScaleName)',
  `brand_scale_name` varchar(255) NULL DEFAULT NULL COMMENT '公司规模',
  `brand_scale_min` varchar(255) NULL DEFAULT NULL COMMENT '公司规模min',
  `brand_scale_max` varchar(255) NULL DEFAULT NULL COMMENT '公司规模max',
  `brand_industry` varchar(255) NULL DEFAULT NULL COMMENT '行业',
  `job_degree` varchar(255) NULL DEFAULT NULL COMMENT '学历',
  `job_experience` varchar(255) NULL DEFAULT NULL COMMENT '工作经验',
  `brand_stage_name` varchar(255) NULL DEFAULT NULL COMMENT '融资阶段',
  `exist_day` int unsigned NOT NULL COMMENT '招聘周期(天数)',
  `third_party_flag` tinyint unsigned NOT NULL DEFAULT '0' COMMENT '是否第三方公司（0正常,1第三方）',
  `source` varchar(255) NOT NULL DEFAULT '0' COMMENT '数据来源(0=boss;1=lagou;2=zhilian;3=qiancheng;4=kanzhun)',
  `welfareList` varchar(2000)  NULL DEFAULT NULL COMMENT '福利',
  `created_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `idx_brand_name_job_name` (`brand_name`,`job_name`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET = utf8mb4 COMMENT='qiancheng job表';


-- 5 平台 job source表
CREATE TABLE `qiancheng_job_source` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT COMMENT '主键id',

  `jobName` varchar(100) DEFAULT NULL COMMENT 'cityDistrict',
  `fullCompanyName` varchar(100) DEFAULT NULL COMMENT 'cityId',
  `jobId` varchar(100) DEFAULT NULL COMMENT 'companyId',
  `jobTags` varchar(255) DEFAULT NULL COMMENT 'companyName',
  `jobAreaString` varchar(100) DEFAULT NULL COMMENT 'companyNumber',
  
  `provideSalaryString` varchar(100) DEFAULT NULL COMMENT 'companySize',
  `workYearString` varchar(255) DEFAULT NULL COMMENT 'companyUrl',
  `degreeString` varchar(100) DEFAULT NULL COMMENT 'education',
  `companyIndustryType1Str` varchar(100) DEFAULT NULL COMMENT 'financingStage_code',
  `companyIndustryType2Str` varchar(100) DEFAULT NULL COMMENT 'financingStage_name',
  
  `lon` varchar(50) DEFAULT NULL COMMENT 'firstPublishTime',
  `lat` varchar(50) DEFAULT NULL COMMENT 'industryCompanyTags',
  `jobHref` varchar(255) DEFAULT NULL COMMENT 'industryName',
  `jobDescribe` varchar(5000) DEFAULT NULL COMMENT 'industryTags',
  `companyHref` varchar(255) DEFAULT NULL COMMENT 'innerBusinessInfo',
  
  `termStr` varchar(100) DEFAULT NULL COMMENT 'jobId',
  `jobWelfareCodeDataList` varchar(500) DEFAULT NULL COMMENT 'jobSummary',
  `jobSalaryMax` varchar(100) DEFAULT NULL COMMENT 'xxx',
  `jobSalaryMin` varchar(255) DEFAULT NULL COMMENT 'positionURL',
  
  `source` text  COMMENT '岗位所有信息',
  
  `created_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `IDK_jobName_fullCompanyName` (`jobName`,`fullCompanyName`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='qiancheng job source表';




