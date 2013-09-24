here=File.dirname(__FILE__)
$home=File.expand_path("#{here}")
require "#{here}/rakefile.rb"

task :setup do
  mkdir_p($include_build_dir)
  mkdir_p($python_build_dir)
  mkdir_p($jar_build_dir)
  mkdir_p($data_home)
  sh "cd tools/slu_core && rake setup BUILD_PREFIX=#{$build_dir}"
  sh "cd data && rake setup"
  sh "rake touch"
  sh "rake everything"
end


task :touch do 
  sh "find tools -mount -name '*.py'"
  sh "find tools -mount -name '*.c'"
  sh "find tools -mount -name '*.java'"
  sh "rm -rf build/last_build"
end



task :default => [:setup, :everything]

task :clean do
  sh "make clean"
end

task :clean_build => [:clean,
                      :everything]
