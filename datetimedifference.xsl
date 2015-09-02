<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:java="java" version="1.0">
  <xsl:template match="/">
    <xsl:variable name="dateFormat" select="java:text.SimpleDateFormat.new('${format string}')" />
    <xsl:variable name="currentdateObject" select="java:parse($dateFormat, .)" />
    <xsl:variable name="expirydateObject" select="java:parse($dateFormat, '${expirydate}')" />
    <xsl:variable name="difference" select="java:getTime($expirydateObject) - java:getTime($currentdateObject)" />
    <datetimedifference>
      <seconds>
        <xsl:value-of select="($difference div 1000)" />
      </seconds>
      <minutes>
        <xsl:value-of select="floor(($difference div (60*1000)))" />
      </minutes>
      <hours>
        <xsl:value-of select="floor(($difference div (60*60*1000)))" />
      </hours>
      <days>
        <xsl:value-of select="floor(($difference div (60*60*24*1000)))" />
      </days>
      <weeks>
        <xsl:value-of select="floor(($difference div (60*60*24*7*1000)))" />
      </weeks>
      <months>
        <xsl:value-of select="floor(($difference div (60*60*24*30*1000)))" />
      </months>
      <years>
        <xsl:value-of select="floor(($difference div (60*60*24*30*12*1000)))" />
      </years>
    </datetimedifference>
  </xsl:template>
</xsl:stylesheet>
