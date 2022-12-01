/**
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.GenericOptionsParser;

public class SQL2MR {

  public static class TokenizerMapper 
       extends Mapper<Object, Text, Text, IntWritable>{
    
    private Text outputKey = new Text();
    private IntWritable outputValue = new IntWritable();
      
    public void map(Object key, Text value, Context context
                    ) throws IOException, InterruptedException {

      String[] toks = value.toString().split(",");

      String carbodyTok = toks[6];
      String mpgTok = toks[toks.length - 2];
      String priceTok = toks[toks.length - 1];

      int mpg = Integer.parseInt(mpgTok);
      float price = Float.parseFloat(priceTok);

      if(price>=10000){
        outputKey.set(carbodyTok);
        outputValue.set(mpg);
        System.out.println("key: "+ outputKey +" mpg: " + mpg  + "price: "+ price);
        context.write(outputKey,outputValue);
      }

      //System.out.println(carbodyTok);
      //System.out.println(mpg);
      //System.out.println(price);

      // note: 
      //  To output from map function,
      //   you need to set output key and value to the instance variables:
      //           outputKey and outputValue, and write it to context
      // see WordCount.java for example
      
      // fill in your code here!!!

	
    }
  }
  
  public static class IntSumReducer 
       extends Reducer<Text,IntWritable,Text,IntWritable> {
    private IntWritable result = new IntWritable();

       private Text outputKey = new Text();

        public void reduce(Text key, Iterable<IntWritable> values, 
                       Context context
                       ) throws IOException, InterruptedException {
      int count=0;
      int max= Integer.MIN_VALUE;
      for(IntWritable value : values) {
            int val = value.get();
            count++;
            max= Math.max(max,val);
        }
      System.out.println("My counter is : "+count);
      outputKey.set(key);
      result.set(max);
      if(count>=5){
        System.out.println("carbody: "+ key + "maxmpg: "+ max);
        context.write(outputKey,result);
      }
	// fill in your code here!!!
    }
  }

  public static void main(String[] args) throws Exception {
    Configuration conf = new Configuration();
    String[] otherArgs = new GenericOptionsParser(conf, args).getRemainingArgs();
    if (otherArgs.length < 2) {
      System.err.println("Usage: sql2mr <in> [<in>...] <out>");
      System.exit(2);
    }
    Job job = Job.getInstance(conf, "sql2mr");
    job.setJarByClass(SQL2MR.class);
    job.setMapperClass(TokenizerMapper.class);
    //job.setCombinerClass(IntSumReducer.class);
    job.setReducerClass(IntSumReducer.class);
    job.setOutputKeyClass(Text.class);
    job.setOutputValueClass(IntWritable.class);
    for (int i = 0; i < otherArgs.length - 1; ++i) {
      FileInputFormat.addInputPath(job, new Path(otherArgs[i]));
    }
    FileOutputFormat.setOutputPath(job,
      new Path(otherArgs[otherArgs.length - 1]));
    System.exit(job.waitForCompletion(true) ? 0 : 1);
  }
}
