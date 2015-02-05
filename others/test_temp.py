# -*- encoding: utf-8 -*-


x = dict()
x['1'] = 2
x['2'] = 4
x['3'] = 8
print x
'''
s = '#{id,jdbcType=VARCHAR}, #{amount,jdbcType=INTEGER}, #{status,jdbcType=INTEGER}, \
      #{createTime,jdbcType=TIMESTAMP}, #{startDate,jdbcType=TIMESTAMP}, #{endDate,jdbcType=TIMESTAMP}, \
      #{coverImage1,jdbcType=VARCHAR}, #{itemId,jdbcType=VARCHAR}, #{itemName,jdbcType=VARCHAR}, \
      #{price,jdbcType=DOUBLE}, #{outletId,jdbcType=VARCHAR}, \
      #{outletName,jdbcType=VARCHAR}, #{cityId,jdbcType=VARCHAR}, \
      #{districtId,jdbcType=VARCHAR}, #{marketId,jdbcType=VARCHAR}, #{mallId,jdbcType=VARCHAR}, \
      #{tagPrice,jdbcType=DOUBLE}, #{review,jdbcType=BIT}, \
      #{expended,jdbcType=BIT}, #{expendTime,jdbcType=TIMESTAMP}, #{order.id,jdbcType=VARCHAR}, \
      #{coverImage2,jdbcType=VARCHAR}, #{coverImage3,jdbcType=VARCHAR}, #{total,jdbcType=DOUBLE}, \
      #{expendCode,jdbcType=VARCHAR}, #{availableDesc,jdbcType=VARCHAR}, #{description,jdbcType=VARCHAR}, \
      #{availableTime,jdbcType=VARCHAR}'
for x in s.split("#"):
    print x.strip()
print len('sdf     '.strip())
 
f = open('/home/lisong/winner.txt')
for x in f:
    print "%s\"); " % x[:-2]
la = [1,2,3]
lb = list()
lb.appendAll(la)
print lb
import uuid
print uuid.uuid1().hex
xx = dict(a=1,b=2,c=3)
print xx
'''