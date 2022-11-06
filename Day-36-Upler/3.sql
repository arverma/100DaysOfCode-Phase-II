-- Codality IAM role Question: Upler


-- create
CREATE TABLE UserRole(
    Id bigint,
    IsEnabled bit, -- 1 if a role is enabled, 0 otherwise
    CreatedBy varchar(200), -- Who created a role
    UpdatedBy varchar(200) -- Who updated a role (if at all)
);

-- insert
INSERT INTO UserRole VALUES (1, 1, 'ADMIN', NULL);
INSERT INTO UserRole VALUES(2, 1, 'ADMIN', 'John Smith');
INSERT INTO UserRole VALUES(3, 0, 'John Smith', 'Ben Smith');
INSERT INTO UserRole VALUES(4, 1, 'Ben Smith', 'Ben Smith');

with eda as(
    select Id, IsEnabled, UPPER(TRIM(CreatedBy)) as UserName, UPPER(TRIM(UpdatedBy)) as UpdatedBy from UserRole
),
created_roles_temp as(
    select UserName, count(Id) as NoOfCreatedRoles, sum(IsEnabled) as IsEnabled_sum from eda group by UserName
),
created_roles as(
select UserName, NoOfCreatedRoles,
    case
      when IsEnabled_sum = 0 THEN -1
      ELSE IsEnabled_sum
    END as NoOfCreatedAndEnabledRoles
from created_roles_temp),
enabled_roles as(
    select UpdatedBy, count(Id) as NoOfUpdatedRoles from eda group by UpdatedBy
)
select c.UserName, c.NoOfCreatedRoles, c.NoOfCreatedAndEnabledRoles, COALESCE(e.NoOfUpdatedRoles, -1) as NoOfUpdatedRoles from created_roles c left join enabled_roles e ON c.UserName = e.UpdatedBy
ORDER BY c.UserName DESC;

